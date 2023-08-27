package br.com.mentalTech;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class UsuariosApplication {

    /*@Autowired
    @Qualifier("applicationName")*/
    @Value("${application.name}")
    private String applicationName;

    @GetMapping("/hello")
    public String HelloWord(){
        return applicationName;
    }
    public static void main(String[] args) {
        SpringApplication.run(UsuariosApplication.class, args);
    }
}
