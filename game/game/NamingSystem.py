class NamingSystem:

    @staticmethod
    def juvenile_name(base_name, sex):
        if sex == "Male":
            return f"Tvsa {base_name}"

        return f"Tkisa {base_name}"

    @staticmethod
    def adult_name(base_name, suffix):
        return f"{base_name}'{suffix}"

    @staticmethod
    def leader_name(base_name, sex):
        if sex == "Male":
            return f"{base_name}'Mane"

        return f"{base_name}'Saber"
