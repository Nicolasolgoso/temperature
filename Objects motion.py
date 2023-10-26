initial_position = float(input("Introduce la posición inicial en metros: "))
initial_velocity = float(input("Introduce la velocidad inicial (m/s): "))
acceleration = float(input("Introduce la aceleración (m/s^2): "))
time = float(input("Introduce el tiempo (s): "))

final_position = initial_position + initial_velocity * time  + 0.5 * acceleration * time * time
velocity = initial_velocity + acceleration * time

print("La posición final es: ", final_position)
print("La velocidad final es: ", velocity)