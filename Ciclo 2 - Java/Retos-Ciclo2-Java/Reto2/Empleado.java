public class Empleado {
    private int id;
    private String nombre;
    private int horasExtra;
    private boolean auxilioTrasporte;
    private int salario;
    
    /* Metodos get y set*/
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getHorasExtra() {
        return horasExtra;
    }

    public void setHorasExtra(int horasExtra) {
        this.horasExtra = horasExtra;
    }

    public boolean isAuxilioTrasporte() {
        return auxilioTrasporte;
    }

    public void setAuxilioTrasporte(boolean auxilioTrasporte) {
        this.auxilioTrasporte = auxilioTrasporte;
    }

    public int getSalario() {
        return salario;
    }

    public void setSalario(int salario) {
        this.salario = salario;
    }
    /* Constructores*/
    public Empleado(){}
    public Empleado(String nombre,int horasExtra, boolean auxilioTrasporte, int salario ){
        this.nombre=nombre;
        this.horasExtra=horasExtra;
        this.auxilioTrasporte=auxilioTrasporte;
        this.salario=salario;
    }
}
