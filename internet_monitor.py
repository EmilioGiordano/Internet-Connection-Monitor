import time
import requests
from datetime import datetime

# Función para generar el nombre del archivo de log
def generate_log_filename(interval):
    start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return f"internet_monitor_{start_time}_interval_{interval}s.log"

# Contador para los números secuenciales
log_counter = 1

def log_message(log_file, message):
    global log_counter
    with open(log_file, "a") as log:
        log.write(f"{log_counter}) {datetime.now()} - {message}\n")
    log_counter += 1  # Incrementar el contador

def check_internet_connection():
    try:
        requests.get("http://www.google.com", timeout=5)
        return True
    except (requests.ConnectionError, requests.Timeout, requests.ReadTimeout):
        return False

def monitor_connection(interval=10):
    log_file = generate_log_filename(interval)
    summary_file = log_file.replace(".log", "_summary.log")
    
    log_message(log_file, "Iniciando monitoreo de conexión a Internet...")
    
    interval_count = 0
    current_state = None
    interval_start_time = datetime.now()
    intervals = []  # Lista para almacenar los intervalos
    
    try:
        while True:
            try:
                is_connected = check_internet_connection()
                new_state = "activa" if is_connected else "perdida"
                
                # Si el estado cambia, registrar el intervalo anterior
                if new_state != current_state:
                    if current_state is not None:  # Ignorar el primer cambio
                        interval_end_time = datetime.now()
                        interval_duration = (interval_end_time - interval_start_time).total_seconds()
                        intervals.append((interval_count, current_state, interval_duration))
                        log_message(log_file, f"Cambio de estado: {current_state} durante {interval_duration:.2f} segundos.")
                    
                    # Iniciar un nuevo intervalo
                    interval_count += 1
                    current_state = new_state
                    interval_start_time = datetime.now()
                
                log_message(log_file, f"Conexión a Internet {new_state}.")
            except Exception as e:
                log_message(log_file, f"Error durante la verificación de conexión: {str(e)}")
            
            time.sleep(interval)
    except KeyboardInterrupt:
        # Registrar el último intervalo al finalizar
        interval_end_time = datetime.now()
        interval_duration = (interval_end_time - interval_start_time).total_seconds()
        intervals.append((interval_count, current_state, interval_duration))
        log_message(log_file, f"Cambio de estado: {current_state} durante {interval_duration:.2f} segundos.")
        
        # Generar el resumen
        summary_message = "Resumen de intervalos:\n"
        for interval_num, state, duration in intervals:
            summary_message += f"Intervalo {interval_num}: {state.capitalize()} durante {duration:.2f} segundos\n"
        
        # Mostrar el resumen en la consola
        print("\n" + summary_message)
        
        # Guardar el resumen en un archivo de log
        with open(summary_file, "w") as summary:
            summary.write(summary_message)
        
        print(f"Resumen guardado en: {summary_file}")

if __name__ == "__main__":
    print("Iniciando monitoreo de conexión a Internet...")
    interval = int(input("Ingresa el intervalo de verificación (en segundos): "))
    monitor_connection(interval)