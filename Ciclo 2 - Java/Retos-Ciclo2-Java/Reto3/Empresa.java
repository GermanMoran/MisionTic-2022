import java.util.ArrayList;
public class Empresa {
    ArrayList<Empleado> empleados = new ArrayList();

    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

    public void setEmpleados(ArrayList<Empleado> empleados) {
        this.empleados = empleados;
    }
    
    public static ArrayList<Double> liquidarNominaEmp(ArrayList<Empleado> empleados){
        ArrayList<Double> liquida = new ArrayList();
        
        int auxilio = 0;
        double totals = 0;
        double valh = 0;

     for(int x= 0; x<empleados.size(); x++){
         
         int salario = empleados.get(x).getSalario();
         int he = empleados.get(x).getHorasExtra();
         
         if(empleados.get(x).isAuxilioTrasporte() == true){
             auxilio=106454;
         }
         else{
             auxilio=0;
         }
        
         valh = salario/240;
         
         totals = (salario+(he*valh));
         
         totals = (totals - (totals*0.08))+ (auxilio);
         
         liquida.add(totals);
        }
     
       return liquida;
    }
    
    public static ArrayList<Double> liquidarParafiscales(ArrayList<Empleado> empleados){
        ArrayList<Double> paraFiscales = new ArrayList();
        
        double totals = 0;
        double valh = 0;

     for(int x= 0; x<empleados.size(); x++){
         
         int salario = empleados.get(x).getSalario();
         int he = empleados.get(x).getHorasExtra();
         
        valh = salario/240;
         
         totals = (salario+(he*valh));
         
         totals = (totals*0.09);
         
         paraFiscales.add(totals);
        }
       return paraFiscales;
    }
    
    /* Liquidar seguridad social*/
    public static ArrayList<Double> liquidarSegSocialEmp(ArrayList<Empleado> empleados){
        ArrayList<Double> liquidasegsoc = new ArrayList();
        
       
        double totals = 0, salud, pension,riesgoslab,seg_soc;
        double valh = 0;

     for(int x= 0; x<empleados.size(); x++){
         
         int salario = empleados.get(x).getSalario();
         int he = empleados.get(x).getHorasExtra();
         
 
        valh = salario/240;
         
         totals = (salario+(he*valh));
         salud = totals*0.085;
         pension = totals*0.12;
         riesgoslab = totals*0.00522;
         seg_soc = salud + pension+riesgoslab;
         
         liquidasegsoc.add(seg_soc);
        }
       return liquidasegsoc;
    }
    
    /* Liquidar prestaciones de la empresa*/
    public static ArrayList<Double> liquidarPrestacionesEmp(ArrayList<Empleado> empleados){
        ArrayList<Double> liquidapresemp = new ArrayList();
        
        double totals = 0, primas, intereses,vacaciones, prestaciones,auxilio,cesantias;
        double valh = 0;

     for(int x= 0; x<empleados.size(); x++){
         
         int salario = empleados.get(x).getSalario();
         int he = empleados.get(x).getHorasExtra();
         
         if(empleados.get(x).isAuxilioTrasporte() == true){
            auxilio=106454;
        }
        else{
            auxilio=0;
        }
        valh = salario/240;
        
        totals = (salario+(he*valh))+auxilio;
        
        primas = totals*0.0833;
        cesantias= totals*0.0833;
        intereses = cesantias*0.12;
        vacaciones = salario*0.0416;
        
        prestaciones = primas+cesantias+intereses+vacaciones;

         
         liquidapresemp.add(prestaciones);
        }
       return liquidapresemp;
    }  
}
