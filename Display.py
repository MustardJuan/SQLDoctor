#Display.py will hold all major output
#Any formatting will be done here
#Additionally design is not permanent and will be updated periodically

def display_welcome():
    print(" $$$$$$\   $$$$$$\  $$\                 $$\   $$\  $$$$$$\  $$\   $$\  $$$$$$\ \n" +
          "$$  __$$\ $$  __$$\ $$ |                $$ |  $$ |$$  __$$\ $$ | $$  |$$  __$$\ \n" +
          "$$ /  \__|$$ /  $$ |$$ |       $$$$$$$\ $$ |  $$ |$$ /  \__|$$ |$$  / $$ /  \__| \n" +
          "\$$$$$$\  $$ |  $$ |$$ |      $$  _____|$$ |  $$ |$$ |      $$$$$  /  \$$$$$$\ \n" +
          " \____$$\ $$ |  $$ |$$ |      \$$$$$$\  $$ |  $$ |$$ |      $$  $$<    \____$$\ \n" +
          "$$\   $$ |$$ $$\$$ |$$ |       \____$$\ $$ |  $$ |$$ |  $$\ $$ |\$$\  $$\   $$ | \n" +
          "\$$$$$$  |\$$$$$$ / $$$$$$$$\ $$$$$$$  |\$$$$$$  |\$$$$$$  |$$ | \$$\ \$$$$$$  | \n" +
          " \______/  \___$$$\ \________|\_______/  \______/  \______/ \__|  \__| \______/  \n" +
          "               \___|                                                             \n" +

          "Disclaimer: Any and all exploits present here are used at the discretion of the user \n" +
          "Latest Version can be found at https://github.com/Mustard1/SQLsUCK \n" +
          "For help with usage enter -h or -help for usage and flags/options available")

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
