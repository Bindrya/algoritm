class PotentialFunctionAnalysis:
    def __init__(self):
        self.phi = 0  # Initial potential function value

    def update_phi(self, value):
        self.phi = value
        return self.phi

    def analyze(self, D, Do):
        # Φ'(D) ≥ 0 байх ёстой
        if D >= Do:
            return True  # Φ'(D) >= 0 бол зөв
        return False  # Хэрэв энэ нөхцөл хангагдахгүй бол буруу

# Жишээ
potential = PotentialFunctionAnalysis()
potential.update_phi(5)
print(potential.analyze(10, 5))  # True
