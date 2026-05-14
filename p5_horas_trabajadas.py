# =================================================================
# FASE 5 - EVALUACIÓN FINAL POA
# Problema 5: Registro y clasificación de horas trabajadas
# =================================================================

def pedir_nombre_completo():
    """Valida y retorna estrictamente un solo nombre y un solo apellido por separado."""
    
    # 1. Validación estricta de UN SOLO Nombre
    while True: 
        nombre = input("Ingrese el nombre del empleado (un solo nombre): ").strip()
        if not nombre: 
            print("  ❌ Error: El nombre no puede estar vacío.")
            continue
        if not all(c.isalpha() or c.isspace() for c in nombre): 
            print("  ❌ Error: Solo se permiten letras.")
            continue
            
        palabras_nombre = nombre.split() 
        # Exigimos estrictamente 1 sola palabra
        if len(palabras_nombre) != 1:
            print("  ❌ Error: Debe ingresar exactamente UN SOLO nombre (sin espacios).")
            continue
        break

    # 2. Validación estricta de UN SOLO Apellido
    while True: 
        apellido = input("Ingrese el apellido del empleado (un solo apellido): ").strip()
        if not apellido: 
            print("  ❌ Error: El apellido no puede estar vacío.")
            continue
        if not all(c.isalpha() or c.isspace() for c in apellido): 
            print("  ❌ Error: Solo se permiten letras.")
            continue
            
        palabras_apellido = apellido.split() 
        # Exigimos estrictamente 1 sola palabra
        if len(palabras_apellido) != 1:
            print("  ❌ Error: Debe ingresar exactamente UN SOLO apellido (sin espacios).")
            continue
        break
        
    # Retorna la unión correcta: "Nombre Apellido"
    return f"{nombre} {apellido}"

def pedir_horas_validas(dia):
    """Valida que las horas ingresadas sean números entre 0 y 15."""
    while True:
        try:
            horas = float(input(f"  Ingrese las horas del {dia}: "))
            if 0 <= horas <= 15:
                return horas
            else:
                print("  ❌ Error: Las horas diarias deben estar entre 0 y 15.")
        except ValueError:
            print("  ❌ Error: Entrada inválida. Ingrese un valor numérico.")

def evaluar_jornada(fila_empleado):
    """
    Recibe la fila de un empleado.
    Calcula el total de horas semanales y clasifica la jornada.
    """
    horas_semanales = fila_empleado[1:] 
    total_horas = sum(horas_semanales)
    
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return total_horas, clasificacion

def main():
    print("=== 🏢 SISTEMA DE CONTROL DE HORAS (RRHH) ===")
    
    matriz_horas =[]
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    
    # 1. MÓDULO DE INGRESO DE DATOS (4 RECURSOS)
    for i in range(4):
        print(f"\n--- Registro del Empleado {i+1} ---")
        nombre_completo = pedir_nombre_completo()
        
        fila_actual = [nombre_completo]
        
        for dia in dias_semana:
            horas_dia = pedir_horas_validas(dia)
            fila_actual.append(horas_dia)
            
        matriz_horas.append(fila_actual)

    # 2. MÓDULO DE SALIDA Y REPORTE
    print("\n" + "="*50)
    print("📊 REPORTE FINAL DE JORNADAS SEMANALES")
    print("="*50)
    
    for fila in matriz_horas:
        nombre = fila[0]
        total_horas, clasificacion = evaluar_jornada(fila)
        
        print(f"👤 Recurso: {nombre.upper()}")
        print(f"   ⏱️ Total Horas: {total_horas} hrs")
        print(f"   🏷️ Clasificación: {clasificacion}\n")

if __name__ == "__main__":
    main()