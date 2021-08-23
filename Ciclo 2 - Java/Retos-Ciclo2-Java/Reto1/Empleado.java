import java.util.ArrayList;
public class Empleado {
    private int id;
    private String nombre;
    private int horasExtra;
    private boolean auxilioTrasporte;
    private int salario;

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
    
    
    public Empleado(){}
    public Empleado(String nombre,int horasExtra, boolean auxilioTrasporte, int salario ){
        this.nombre=nombre;
        this.horasExtra=horasExtra;
        this.auxilioTrasporte=auxilioTrasporte;
        this.salario=salario;
    }
    
    public static ArrayList<Double> liquidarNominaQuincenal(ArrayList<Empleado> empleados){
        ArrayList<Double> liquida = new ArrayList();
        int auxilio = 0;
        double totals = 0;
        double valh = 0;

     for(int x= 0; x<empleados.size(); x++){
         
         int salario = empleados.get(x).salario;
         int he = empleados.get(x).horasExtra;
         
         if(empleados.get(x).auxilioTrasporte == true){
             auxilio=106454;
         }
         else{
             auxilio=0;
         }
        
        
         valh = salario/240; 
         totals = (salario+(he*valh))/2;
         totals = (totals - (totals*0.08))+ (auxilio/2);
         liquida.add(totals);
        }
     
       return liquida;
    }   
}
