package com.ciclo4.purchase.controller;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.User;
import com.ciclo4.purchase.service.UserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/api/user")
@CrossOrigin
public class UserController {
    
    @Autowired
    private UserService servicio;


    /**
     * Servicios GET
     * 
     */
    /** */
    @GetMapping("")
    public String demo(){
        return "String Test";
    }
    @GetMapping("/all")
    public List<User> demo2(){
        return servicio.getAll();
    }

    /*@GetMapping("/{id}")
    public Optional<User> getUser(@PathVariable Integer id){
        return servicio.getUserById(id);
    }*/
    @GetMapping("/{email}")
    public boolean getUser(@PathVariable String email){
        System.out.println(servicio.getUserByEmail(email));
        if(servicio.getUserByEmail(email).isEmpty()){
            return false;
        }else{
            return true;
        }
    }
    @GetMapping("/{user_email}/{user_password}")
    public User getAuth(@PathVariable String user_email,@PathVariable String user_password){
        Optional<User> check=servicio.checkAuth(user_email,user_password);
        User user;
        try {
            user=check.get();
        } catch (Exception e) {
            user=new User();
            user.setEmail(user_email);
            user.setPassword(user_password);
            user.setName("NO DEFINIDO");
            user.setId(null);
        }
        System.out.println(check);
        return user;
        
    }
    /**
     * Servicios POST
     * 
     */
    /** */
    /**
     * 
     * @param user
     * @return
     */
    @PostMapping("/new")
    @ResponseStatus(HttpStatus.CREATED)
    @CrossOrigin
    public Optional<User> save(@RequestBody User user){
        return servicio.saveUser(user);
    }

    /**
     * 
     */
    @DeleteMapping("/all")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void deleteAll(){
        servicio.deleteAll();
    }    
    
}