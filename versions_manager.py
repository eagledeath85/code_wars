class VersionManager:
    def __init__(self, initial_version=''):
        if initial_version:
            version = initial_version.split('.')
            if len(version) > 2:
                version = version[:3]
            try:
                self.major_version = int(version[0])
                self.minor_version = int(version[1]) if len(version) > 1 else 0
                self.patch_version = int(version[2]) if len(version) > 2 else 0
            except ValueError:
                raise Exception("Error occured while parsing version!")
        else:
            self.major_version = 0
            self.minor_version = 0
            self.patch_version = 1

        self.versions_history = []

    def major(self, value=1):
        self.versions_history.append((self.major_version, self.minor_version, self.patch_version))
        self.major_version += value
        self.minor_version = 0
        self.patch = 0
        return self

    def minor(self, value=1):
        self.versions_history.append((self.major_version, self.minor_version, self.patch_version))
        self.minor_version += value
        self.patch = 0
        return self

    def patch(self, value=1):
        self.versions_history.append((self.major_version, self.minor_version, self.patch_version))
        self.patch += value
        return self

    def rollback(self):
        # "1.1.1" -> '1.1.0'
        if self.versions_history:
            self.major_version, self.minor_version, self.patch_version = self.versions_history.pop()
        else:
            raise Exception("Cannot rollback!")
        return self

    def release(self):
        return f"{self.major_version}.{self.minor_version}.{self.patch_version}"


v = VersionManager("1")
print(v.release())

