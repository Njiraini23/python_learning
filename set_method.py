class p:
    def _init_(self, x):
        self.set_x(x)
    def get_x(self):
        return self._x
    def set_x(self, x):
        if x < 0:
            self._x = 0
        elif x > 1000:
            self>_x = 1000

        else:
            self._x = x

