class VersionManager:
    def __init__(self, initial_version=''):

        self.version = initial_version
        self.release_history = []
        version_components = self.version.split(".")
        for i in range(len(version_components)):
            if not version_components[i].isdigit():
                raise ValueError("Error occured while parsing version!")

        self.release_history.append(self.version)

        if len(version_components) == 1:
            self.version = int(version_components[0])
        elif len(version_components) == 2:
            self.version = [
                int(version_components[0]),
                int(version_components[1])
            ]
        else:
            self.version = [
                int(version_components[0]),
                int(version_components[1]),
                int(version_components[2])
            ]

    def major(self, value=1):
        self.version[0] += value
        self.version[1] = 0
        self.version[2] = 0
        return self

    def minor(self, value=1):
        self.version[1] += value
        self.version[2] = 0
        return self

    def patch(self, value=1):
        self.version[2] += value
        return self

    def rollback(self):
        # "1.1.1" -> '1.1.0'
        if self.release_history is None:
            raise Exception("Cannot rollback!")
        self.version = self.release_history.pop()
        return self

    def release(self):

        release = str(f'{self.major()}.{self.minor()}.{self.patch()}')

        return release


version = VersionManager("1").release()

