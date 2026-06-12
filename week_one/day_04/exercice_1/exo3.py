import numpy as np


class BroadcastingDemo:
    """Demonstration of NumPy broadcasting concepts"""

    def __init__(self):
        self.matrix_3x3 = np.array([[1, 2, 3],
                                    [4, 5, 6],
                                    [7, 8, 9]])
        self.vector = np.array([10, 20, 30])
        self.vector_col = self.vector.reshape(3, 1)
        self.a = np.array([[1], [2], [3], [4]])
        self.b = np.array([[10, 20, 30]])

    def example1_row_broadcasting(self):
        """Example: Matrix (3,3) + Vector (3), - row broadcasting"""
        result = self.matrix_3x3 + self.vector
        return result

    def example2_column_broadcasting(self):
        """Example: Matrix (3,3) + Vector (3,1) - column broadcasting"""
        result = self.matrix_3x3 + self.vector_col
        return result

    def example3_matrix_broadcasting(self):
        """Example: Matrix (4,1) + Matrix (1,3)"""
        result = self.a + self.b
        return result

    def display_example1(self):
        """Display example 1"""
        print("\n1. Matrix (3,3) + Vector (3,)")
        print(f"Matrix:\n{self.matrix_3x3}")
        print(f"Vector: {self.vector}")
        print(f"Result (broadcasting):\n{self.example1_row_broadcasting()}")
        print("Broadcasting: Vector added to each ROW")

    def display_example2(self):
        """Display example 2"""
        print("\n2. Matrix (3,3) + Vector (3,1)")
        print(f"Vector (column):\n{self.vector_col}")
        print(f"Result:\n{self.example2_column_broadcasting()}")
        print("Broadcasting: Vector added to each COLUMN")

    def display_example3(self):
        """Display example 3"""
        print("\n3. Matrix (4,1) + Matrix (1,3)")
        print(f"A (4,1):\n{self.a}")
        print(f"B (1,3):\n{self.b}")
        print(f"Result (4,3):\n{self.example3_matrix_broadcasting()}")

    def run_all_demos(self):
        """Run all broadcasting demonstrations"""
        print("=" * 60)
        print("BROADCASTING EXAMPLES")
        print("=" * 60)

        self.display_example1()
        self.display_example2()
        self.display_example3()

        print("\n" + "=" * 60)
        print("END OF DEMONSTRATION")
        print("=" * 60)


# Main execution
if __name__ == "__main__":
    demo = BroadcastingDemo()
    demo.run_all_demos()
