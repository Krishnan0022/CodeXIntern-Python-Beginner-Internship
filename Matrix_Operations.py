import numpy as np

stored_matrices = {}

def display_menu():
    print("\nMatrix Operations Tool")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Transpose Matrix")
    print("5. Calculate Determinant")
    print("6. Calculate Inverse")
    print("7. View Stored Matrices")
    print("8. Clear Stored Matrices")
    print("9. Exit")

def format_matrix(matrix):
    return "\n".join(["\t".join(map("{:.2f}".format, row)) for row in matrix])

def get_matrix(prompt, save_key=None):
    print(prompt)
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    print(f"Enter the elements row by row ({rows}x{cols}):")
    elements = []
    for _ in range(rows):
        row = list(map(float, input().split()))
        if len(row) != cols:
            raise ValueError(f"Each row must have exactly {cols} elements.")
        elements.append(row)
    matrix = np.array(elements)
    if save_key:
        stored_matrices[save_key] = matrix
    return matrix

def view_matrices():
    if not stored_matrices:
        print("No matrices stored.")
        return
    print("\nStored Matrices:")
    for key, matrix in stored_matrices.items():
        print(f"{key}:\n{format_matrix(matrix)}\n")

def clear_matrices():
    stored_matrices.clear()
    print("All stored matrices have been cleared.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-9): ")

        try:
            if choice == "1":
                matrix1 = get_matrix("Enter the first matrix:")
                matrix2 = get_matrix("Enter the second matrix:")
                if matrix1.shape != matrix2.shape:
                    print("Error: Matrices must have the same dimensions for addition.")
                else:
                    result = matrix1 + matrix2
                    print("Result of Addition:")
                    print(format_matrix(result))

            elif choice == "2":
                matrix1 = get_matrix("Enter the first matrix:")
                matrix2 = get_matrix("Enter the second matrix:")
                if matrix1.shape != matrix2.shape:
                    print("Error: Matrices must have the same dimensions for subtraction.")
                else:
                    result = matrix1 - matrix2
                    print("Result of Subtraction:")
                    print(format_matrix(result))

            elif choice == "3":
                matrix1 = get_matrix("Enter the first matrix:")
                matrix2 = get_matrix("Enter the second matrix:")
                if matrix1.shape[1] != matrix2.shape[0]:
                    print("Error: The number of columns of the first matrix must equal the number of rows of the second matrix.")
                else:
                    result = np.dot(matrix1, matrix2)
                    print("Result of Multiplication:")
                    print(format_matrix(result))

            elif choice == "4":
                matrix = get_matrix("Enter the matrix to transpose:")
                result = matrix.T
                print("Transpose of the Matrix:")
                print(format_matrix(result))

            elif choice == "5":
                matrix = get_matrix("Enter the square matrix to calculate determinant:")
                if matrix.shape[0] != matrix.shape[1]:
                    print("Error: Determinant can only be calculated for square matrices.")
                else:
                    determinant = np.linalg.det(matrix)
                    print("Determinant of the Matrix:")
                    print(f"{determinant:.2f}")

            elif choice == "6":
                matrix = get_matrix("Enter the square matrix to calculate inverse:")
                if matrix.shape[0] != matrix.shape[1]:
                    print("Error: Inverse can only be calculated for square matrices.")
                elif np.linalg.det(matrix) == 0:
                    print("Error: Singular matrices do not have an inverse.")
                else:
                    result = np.linalg.inv(matrix)
                    print("Inverse of the Matrix:")
                    print(format_matrix(result))

            elif choice == "7":
                view_matrices()

            elif choice == "8":
                clear_matrices()

            elif choice == "9":
                print("Exiting the Matrix Operations Tool. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
