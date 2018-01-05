from util.path_abstract import PathAbstract


class Path(PathAbstract):
    @staticmethod
    def db_root_dir():
        return '/media/eec/external/Databases/Segmentation/DAVIS-2016/'

    @staticmethod
    def save_root_dir():
        return './models'

    @staticmethod
    def models_dir():
        return "/home/eec/PycharmProjects/models"

