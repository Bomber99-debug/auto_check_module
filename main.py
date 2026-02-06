from log import log_info, log_warning, log_error
import math

def calculate_square_root(numgers:list) -> None:
    for number in numgers:
        try:
            if number < 0:
                # Логування попередження для від'ємних чисел
                log_warning(f"Знайдено від'ємне число: {number}. Пропускаємо.")
                continue
            root = math.sqrt(number)
            log_info(f"Квадратний корінь з {number} {root:.2f}")
        except Exception as e:
            # Логування помилки у випадку інших винятків
            log_error(f"Помилка при обчисленні кореня для {number}: {e}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Припустимо, у нас є список чисел
    numbers = [16, -4, 9, 25, 0, 4, "16"]
    calculate_square_root(numbers)

