; Código hecho por: Cuevas Romero Desire y Hernández Méndez Gerardo Antonio. Grupo 3BV2. Paradigmas de Programación.
; Se define una función llamada factorial que toma un argumento "n".
(defun factorial (n)
  ; Si n es mayor que 1, se evalúa recursivamente para calcular el factorial.
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

(defparameter input 5) ; Valor de n asignado directamente

; Muestra el resultado del cálculo del factorial
(format t "El factorial de ~a es: ~a" input (factorial input))