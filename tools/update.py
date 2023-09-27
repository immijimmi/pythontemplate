from os import chdir
from subprocess import run, check_output
from typing import Optional

# Change this value to a valid tag to exclude any tags that are chronologically before it from the available options
TAGS_START_FROM: Optional[str] = None
# Add valid tags to this set to exclude them from the available options
TAGS_BLACKLIST = set(

)


def get_chronological_tags() -> list[str]:
    output_str = check_output("git tag --sort=creatordate").decode("UTF-8")

    tags_list = output_str.split("\n")
    tags_list.remove("")  # Remove blank string caused by trailing newline character

    return tags_list


def filter_tags(
        chronological_tags: list[str],
        start_from: Optional[str] = None, blacklist: set[str] = set()
) -> list[str]:
    result = []

    is_past_start = (True if (start_from is None) else False)
    for tag in chronological_tags:
        if not is_past_start:
            if tag == start_from:
                is_past_start = True
            else:
                continue

        if tag in blacklist:
            continue

        result.append(tag)

    return result


def prompt_for_tag(tags: set[str]) -> Optional[str]:
    while True:
        user_input_tag = input("Type in the version you wish to use, and press Enter:").strip()

        if user_input_tag in tags:
            return user_input_tag
        else:
            print("\nUnable to find a version with that tag.")


chdir("..")
run("git fetch")

processed_tags = filter_tags(get_chronological_tags(), start_from=TAGS_START_FROM, blacklist=TAGS_BLACKLIST)
if processed_tags:
    print("Available versions:\n{}\n".format('\n'.join(processed_tags)))

    selected_tag = prompt_for_tag(set(processed_tags))
    if selected_tag:
        checkout_output = check_output(f"git checkout {selected_tag}").decode("UTF-8")
        if "Aborting" in checkout_output:
            if "Please commit your changes" in checkout_output:
                print(
                    "\nYou've made unsaved changes to this project. "
                    "Are you sure you want to discard them and switch version?"
                )
                user_input_discard = input(
                    "Type 'discard' and press Enter to continue, "
                    "or just press Enter to cancel and leave your files as-is:"
                )

                if user_input_discard == "discard":
                    run(f"git checkout {selected_tag} --force")
                    print(f"\nSwitched to: {selected_tag}")

            else:
                print("\nAn unknown error has occurred. No changes have been made.")
                print(f"Full output:\n\n{checkout_output}")

        else:
            print(f"\nSwitched to: {selected_tag}")

else:
    print("No available versions found.")

input("\nEnter to quit:")
