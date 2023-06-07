class VersionManager:
    def __init__(self, initial_version=''):
        if initial_version:
            version_parts = initial_version.split('.')
            if len(version_parts) > 2:
                version_parts = version_parts[:3]

            try:
                self.major_version = int(version_parts[0])
                self.minor_version = int(version_parts[1]) if len(version_parts) > 1 else 0
                self.patch_version = int(version_parts[2]) if len(version_parts) > 2 else 0
            except ValueError:
                raise Exception("Error occurred while parsing version!")
        else:
            self.major_version = 0
            self.minor_version = 0
            self.patch_version = 1

        self.release_history = []

    def major(self, value=1):
        self.release_history.append((self.major_version, self.minor_version, self.patch_version))
        self.major_version += value
        self.minor_version = 0
        self.patch_version = 0
        return self

    def minor(self, value=1):
        self.release_history.append((self.major_version, self.minor_version, self.patch_version))
        self.minor_version += value
        self.patch_version = 0
        return self

    def patch(self, value=1):
        self.release_history.append((self.major_version, self.minor_version, self.patch_version))
        self.patch_version += value
        return self

    def rollback(self):
        # "1.1.1" -> '1.1.0'
        if self.release_history:
            self.major_version, self.minor_version, self.patch_version = self.release_history.pop()
        else:
            raise Exception("Cannot rollback!")
        return self

    def release(self):
        return f"{self.major_version}.{self.minor_version}.{self.patch_version}"


print(VersionManager().major().patch().rollback().release())