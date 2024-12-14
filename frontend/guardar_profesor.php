<?php
// Configuración de la base de datos
$host = "localhost"; 
$user = "root"; 
$password = ""; 
$database = "registro_profesor";

// Conexión a la base de datos
$conn = new mysqli($host, $user, $password, $database);

// Verificar conexión
if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

// Capturar datos del formulario
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    $correo = $_POST['correo'];
    $contraseña = password_hash($_POST['contraseña'], PASSWORD_BCRYPT); // Encriptar contraseña
    $direccion = $_POST['direccion'];
    $departamento = $_POST['departamento'];
    $id = $_POST['id'];
    $codigo_profesor = $_POST['codigo_profesor'];
    $telefono = $_POST['telefono'];
    $codigo_clase = $_POST['codigo_clase'];

    // Insertar datos en la tabla
    $sql = "INSERT INTO profesores (nombre, correo, contraseña, direccion, departamento, id, codigo_profesor, telefono, codigo_clase) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssssssss", $nombre, $correo, $contraseña, $direccion, $departamento, $id, $codigo_profesor, $telefono, $codigo_clase);

    if ($stmt->execute()) {
        echo "Registro exitoso. ¡Bienvenido!";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
}

$conn->close();
?>
