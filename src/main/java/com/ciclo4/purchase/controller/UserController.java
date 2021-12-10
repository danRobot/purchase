package com.ciclo4.purchase.controller;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.User;
import com.ciclo4.purchase.service.UserService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/helloREST")
public class UserController {
    
    @Autowired
    private UserService servicio;

    @GetMapping("")
    public String demo(){
        return "String Test";
    }
    @GetMapping("/all")
    public List<User> demo2(){
        return servicio.getAll();
    }
    @GetMapping("/b")
    public float demo3(){
        User u=new User();
        u.setEmail("email");
        u.setName("name");
        u.setPassword("password");
        servicio.saveUser(u);
        return 0.0f;
    }
    @GetMapping("/user/{id}")
    public Optional<User> getUser(@PathVariable Integer id){
        return servicio.getUser(id);
    }
    @GetMapping("/c/{id}/{user_email}/{name}/{password}")
    public float demo4(@PathVariable Integer id,@PathVariable String user_email,@PathVariable String name,@PathVariable String password){
        User u=new User();
        u.setId(id);
        u.setEmail(user_email);
        u.setName(name);
        u.setPassword(password);
        servicio.saveUser(u);
        return 0.0f;
    }
    
}
class Test{
    Test(){

    }
    private float a;
    private String name;
    private String email;
    public float getA(){
        return a;
    }
    public String getName(){
        return name;
    }
    public String getEmail(){
        return email;
    }
    public void setA(float a){
        this.a=a;
    }
    public void setName(String name){
        this.name=name;
    }
    public void setEmail(String email){
        this.email=email;
    }
}