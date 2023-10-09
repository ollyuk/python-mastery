class Tp:
    class_level_var = 0

    def __init__(self, instance_var):
        self.instance_var = instance_var

    @classmethod
    def set_class_level(cls, x):
        cls.class_level_var = x
