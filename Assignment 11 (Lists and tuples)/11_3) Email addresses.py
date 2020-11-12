def get_emails():
    email_list = []

    while True:
        email = input("Email address: ").strip()
        if email != 'q':
            email_list.append(email)
        else:
            break
    
    return email_list

def get_names_and_domains(email_list):
    names_and_domains = []

    for person in email_list:
        name_email = []
        index = 0

        # Find index of '@'
        for char in person:
            if char == '@':
                break
            else:
                index += 1
        
        name_email.append(person[:index]) # Name
        name_email.append(person[(index+1):]) # Domain

        t_name_email = tuple(name_email)
        names_and_domains.append(t_name_email)
    
    return names_and_domains

# Main program starts here - DO NOT change it
email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)