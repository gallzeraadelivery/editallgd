package com.example.fingerprintspoof;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.io.DataOutputStream;
import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private static final String TAG = "FingerprintSpoof";
    
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Inicializar componentes da UI
        Button btnSpoofFingerprint = findViewById(R.id.btnSpoofFingerprint);
        TextView txtStatus = findViewById(R.id.txtStatus);
        
        // Configurar botão de spoofing
        btnSpoofFingerprint.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                spoofFingerprint();
            }
        });
    }
    
    /**
     * Método para spoofar os fingerprints do dispositivo
     */
    private void spoofFingerprint() {
        Log.d(TAG, "Iniciando spoofing de fingerprint...");
        
        try {
            // Verificar se o dispositivo tem root
            if (isDeviceRooted()) {
                Toast.makeText(this, "Dispositivo com root detectado", Toast.LENGTH_LONG).show();
                
                // Executar comandos de spoofing
                spoofSystemProperties();
                
                Toast.makeText(this, "Spoofing concluído!", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(this, "Dispositivo não possui root", Toast.LENGTH_LONG).show();
            }
        } catch (Exception e) {
            Log.e(TAG, "Erro durante spoofing: " + e.getMessage());
            Toast.makeText(this, "Erro: " + e.getMessage(), Toast.LENGTH_LONG).show();
        }
    }
    
    /**
     * Spoof dos dados do sistema (build properties)
     */
    private void spoofSystemProperties() {
        try {
            // Comandos para modificar propriedades do sistema
            Process process = Runtime.getRuntime().exec("su");
            DataOutputStream os = new DataOutputStream(process.getOutputStream());
            
            // Modificar informações do build
            os.writeBytes("setprop ro.product.model \"NewModel\"\n");
            os.writeBytes("setprop ro.product.brand \"NewBrand\"\n");
            os.writeBytes("setprop ro.product.name \"NewName\"\n");
            os.writeBytes("setprop ro.product.device \"NewDevice\"\n");
            os.writeBytes("setprop ro.build.fingerprint \"new/fingerprint/123456\"\n");
            os.writeBytes("setprop ro.build.display.id \"NewDisplayID\"\n");
            
            os.flush();
            os.close();
            
            process.waitFor();
            
            Log.d(TAG, "Propriedades do sistema modificadas com sucesso");
            
        } catch (Exception e) {
            Log.e(TAG, "Erro ao modificar propriedades do sistema: " + e.getMessage());
        }
    }
    
    /**
     * Verifica se o dispositivo está rootado
     */
    private boolean isDeviceRooted() {
        String[] paths = {"/system/app/Superuser.apk", "/sbin/su", "/system/bin/su", 
                       "/system/xbin/su", "/data/local/xbin/su", "/data/local/bin/su", 
                       "/system/sd/xbin/su", "/system/bin/failsafe/su", 
                       "/data/local/su"};
        
        for (String path : paths) {
            if (new java.io.File(path).exists()) {
                return true;
            }
        }
        return false;
    }
}