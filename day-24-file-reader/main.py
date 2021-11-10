# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

def create_invitations(names, invitation_template):
    for name in names:
        # Remove enter or the '\n' char from names
        clean_name = name.strip()
        with open(f"./Output/ReadyToSend/invitation_for_{clean_name}.txt", "w+") as invitation:
            new_invitation = invitation_template.replace(
                "[name]", clean_name)
            invitation.write(new_invitation)


if __name__ == '__main__':
    names = []
    invitation_template = ''
    with open("./Input/Names/invited_names.txt", "r") as file:
        names = file.readlines()

    with open("./Input/Letters/starting_letter.txt", "r") as template:
        invitation_template = template.read()

    create_invitations(names, invitation_template)
