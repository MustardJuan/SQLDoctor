#Display.py will hold all major output
#Any formatting will be done here
#Additionally design is not permanent and will be updated periodically

def display_welcome():
    print("\n\n\n" +
	  "  ____    _____   __               __  __  ____     __  __      \n" +
	  " /\  _`\ /\  __`\/\ \             /\ \/\ \/\  _`\  /\ \/\ \     \n" +
	  " \ \,\L\_\ \ \/\ \ \ \        ____\ \ \ \ \ \ \/\_\\ \ \/'/'    \n" +
	  "  \/_\__ \\ \ \ \ \ \ \  __  /',__\\ \ \ \ \ \ \/_/_\ \ , <     \n" +
	  "     /\ \L\ \ \ \\'\\ \ \L\ \/\__, `\\ \ \_\ \ \ \L\ \\ \ \\`\   \n" +
	  "   \ `\____\ \___\_\ \____/\/\____/ \ \_____\ \____/ \ \_\ \_\ \n" +
	  "    \/_____/\/__//_/\/___/  \/___/   \/_____/\/___/   \/_/\/_/ \n" +
          "                                                               \n\n" +
          "Legal Disclaimer: Any and all exploits present here are used at the discretion of the user\n" +
	  "Additionally, it is the user's responsibility to obey all applicable law, local, state and federal\n" +
	  "All developers involved assume no liability and are not responsible for misuse or damage due to the use of this software\n" +
          "Latest Version can be found at https://github.com/Mustard1/SQLsUCK \n" +
          "For help with usage enter -h or -help for usage and flags/options available\n\n\n")

def display_help():
    print("Takes [OPTIONS] [URL] {payload name} \n" +
          "-F will fingerprint the database that is present on the web application if it exists \n" +
          "-X will execute the specified payload on the victim URL \n" +
          "-A will automatically run default sequences: fingerprinting followed by most popular injections \n" +
          "More options to come later~")

def display_fingerprint():
    print("Whoop there's nothing here my guy")

def display_uniq_attack():
    print("Whoop not quite yet my dude")

def display_attack():
    print("DEPLOYING ASSUALT SQUAD")
