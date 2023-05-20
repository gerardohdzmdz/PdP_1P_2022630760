; Código hecho por: Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2. Paradigmas de Programación.
; La funcion fibonacci recibe un numero "n"
(defun fibonacci (n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (t (+ (fibonacci (- n 1))
              (fibonacci (- n 2))))))
; La funcion imprimir-fibonacci imprime los primeros n términos de la secuencia
(defun imprimir-fibonacci (n)
; Se usa la funcion dotimes para iterar de 0-10
  (dotimes (i n)
    (format t "~a " (fibonacci i))))

; Ejemplo de uso
(imprimir-fibonacci 10)