from sympy import diff


def function(x1_, x2_):
    string_function_f = '3*x1**2 + 2*x2**2 - 10'
    func_ = eval(string_function_f, {'x1': x1_, 'x2': x2_})
    return func_


# нужно для пеналти
def composing_function_p_penalty_method(r_):
    string_function_f = '3*x1**2 + 2*x2**2 - 10'
    string_function_g = 'x1 + 2*x2 - 6'
    string_function_p = string_function_f + " + " + str(r_ / 2) + "*(" + string_function_g + ")**2"
    return string_function_p


# (град)
def count_function_p(string_function_p, x1_, x2_):
    func_p = eval(string_function_p, {'x1': x1_, 'x2': x2_})
    return func_p


# (штраф)
def final_count_func_p_penalty_method(r_, x1_, x2_):
    string_function_g = 'x1 + 2*x2 - 6'
    string = f'{r_ / 2} * ({string_function_g})**2'
    answer = eval(string, {'x1': x1_, 'x2': x2_})
    return answer


# нужно для пеналти (град)
def composing_function_grad_x1(string_function_p):
    string_grad_x1 = str(diff(string_function_p, 'x1'))
    return string_grad_x1


# нужно для пеналти (град)
def composing_function_grad_x2(string_function_p):
    string_grad_x2 = str(diff(string_function_p, 'x2'))
    return string_grad_x2


# (град)
def gradient_x1(string_grad_x1, x1_, x2_):
    grad_x1_ = eval(string_grad_x1, {'x1': x1_, 'x2': x2_})
    return grad_x1_


# (град)
def gradient_x2(string_grad_x2, x1_, x2_):
    grad_x2_ = eval(string_grad_x2, {'x1': x1_, 'x2': x2_})
    return grad_x2_


# (град)
def norm_of_vector(x1_, x2_):
    norm_x_ = (x1_ ** 2 + x2_ ** 2) ** (1 / 2)
    return norm_x_


def method_gradient_descent_constant_step(string_function_p, x1_, x2_, t_):
    set_value_m_ = 10
    eps1_ = 0.15
    eps2_ = 0.2
    k_ = 0
    flag_ = 0
    print(f'     *M = {set_value_m_}, eps1 = {eps1_}, eps2 = {eps2_}, x = ({round(x1_, 4)};{round(x2_, 4)})')
    print('     ', '-' * 64)
    while True:
        count_t = 0
        print('     *сk =', k_, '; x1 =', round(x1_, 5), ', x2 =', round(x2_, 5))

        print('     ', '-' * 64)
        if flag_ == 2:
            print(f'     *X({k_}) и X({k_ - 1}) подходят')
            print('     *Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                  round(count_function_p(string_function_p, x1_, x2_), 5))
            break
        else:
            string_grad_x1 = composing_function_grad_x1(string_function_p)
            string_grad_x2 = composing_function_grad_x2(string_function_p)
            grad_x1 = gradient_x1(string_grad_x1, x1_, x2_)
            grad_x2 = gradient_x2(string_grad_x2, x1_, x2_)
            norma_vectors = norm_of_vector(grad_x1, grad_x2)
            print('     *Градиент = (', round(grad_x1, 5), ':', round(grad_x2, 5), ')  ; нармаль вектора =',
                  round(norma_vectors, 5))
            if norma_vectors < eps1_:
                print('     * Т.к norm_vector < eps1')
                print()
                print('     ', '-' * 64)
                print('     *Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                      round(count_function_p(string_function_p, x1_, x2_), 5))
                break
            else:
                if k_ >= set_value_m_:
                    print('     Т.к k >= M, то: ')
                    print('     *Ответ: x1 =', round(x1_, 5), '; x2 =', round(x2_, 5), '; func = ',
                          round(count_function_p(string_function_p, x1_, x2_), 5))
                    break
                else:
                    while True:
                        count_t += 1
                        print('     ', count_t, '. t =', t_)
                        x1_next = x1_ - t_ * grad_x1
                        x2_next = x2_ - t_ * grad_x2

                        print(f'     X({k_ + 1}) = (', round(x1_next, 5), ':', round(x2_next, 5), ')')
                        print(f'     f(X({k_ + 1})) = ', round(count_function_p(string_function_p,
                                                                                x1_next, x2_next), 5))
                        print('     f(x) =', round(count_function_p(string_function_p, x1_, x2_), 5))
                        if count_function_p(string_function_p, x1_next, x2_next) - count_function_p(string_function_p,
                                                                                                    x1_, x2_) < 0:
                            print(f'     f(X({k_ + 1})) - f(X) < 0')
                            break
                        else:
                            print(f'     Т.к f(X({k_ + 1}) - f(X) > 0, то')
                            t_ = t_ / 2
                            print(f'      t = t/2: t = {t_}')
                            print('    ', '- ' * 33)

                    for_norm_vector_x1 = x1_next - x1_
                    for_norm_vector_x2 = x2_next - x2_
                    if abs(count_function_p(string_function_p, x1_next, x2_next) - count_function_p(string_function_p,
                                                                                                    x1_, x2_)) < eps2_ \
                            and norm_of_vector(for_norm_vector_x1, for_norm_vector_x2) < eps2_:
                        print(f'     * Заметим ||X({k_ + 1}) -X({k_})|| < eps2 and f(X({k_ + 1}) - f(X) < eps2')
                        flag_ += 1
                        print('     *flag = ', flag_)
                    else:
                        print(f'     * Заметим ||X({k_ + 1}) -X({k_})|| > eps2 or f(X({k_ + 1}) - f(X) > eps2')
                        flag_ = 0
                        print('     *flag = ', flag_)
                    k_ += 1
                    x1_ = x1_next
                    x2_ = x2_next
                    print('     ', '-' * 64)
    return x1_, x2_, t_


def main():
    eps = 0.05
    r = 0.5
    С = 8

    x1 = 0.5
    x2 = 0
    k = 0
    t = 0.25
    print(f'\nНачальные условия: {r = }, C = {С}, {eps = }, x0 = ({x1};{x2})')
    while True:
        print(f'\n---------------Итерация {k = }---------------\n')
        print(f'{r = }, x = ({round(x1, 4)};{round(x2, 4)})')
        string_function_p = composing_function_p_penalty_method(r)
        print('F(x;r0) =', string_function_p)

        print('\nПоиск минимума методом градиентного спуска с постоянным шагом\n', '-' * 64)
        list_answer_x = method_gradient_descent_constant_step(string_function_p, x1, x2, t)
        x1_new = list_answer_x[0]
        x2_new = list_answer_x[1]
        t = list_answer_x[2]

        print('    ' + '-' * 64 + '\n' + f'Отсюда x* = ({round(x1_new, 4)};{round(x2_new, 4)})')
        value_func_p = final_count_func_p_penalty_method(r, x1_new, x2_new)
        print('P(x(r), r) =', round(value_func_p, 4))
        print('')

        if value_func_p <= eps:
            print(f'Т.к {round(value_func_p, 5)} < {eps} => конец процесса поиска')

            print('    ', '=' * 60 + f'\n'
                                     f'    | Ответ'
                                     f'\n'
                                     f'    | x = ({round(x1_new, 4)};{round(x2_new, 4)})'
                                     f'\n'
                                     f'    | f(x) = {round(function(x1_new, x2_new), 4)}\n' + '    | ' + '=' * 60, '\n')
            break
        else:
            r *= С
            k += 1
            x1 = x1_new
            x2 = x2_new
            print(f'{round(value_func_p, 2)} > {eps} => r = r*C = {r}, x=({round(x1_new, 4)};{round(x2_new, 4)})')
            print('')
    return 0


if __name__ == "__main__":
    print("\nМетоды условной оптимизации. Поиск локального минимума функции.\n\n")

    main()