package com.ciclo4.purchase.service;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.User;
import com.ciclo4.purchase.reposotory.UserRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private UserRepository repositorio;

    /**
     * Devuelve todos los usuarios de la base de datos
     * @return
     */
    public List<User> getAll(){
        return repositorio.findAll();
    }
    
    /**
     * Añade un Usuario a la base de Datos
     * @param user
     * @return
     */
    public User saveUser(User user){
        return repositorio.save(user);
    }

    /**
     * Busca un usuario por el Correo
     * @param email
     * @return
     */
    public Optional<User> getUserByEmail(String email){
        return repositorio.getUserByEmail(email);
    }
    
    /**
     * Busca un usuario por el Nombre
     * @param name
     * @return
     */
    public Optional<User> getUserByName(String name){
        return repositorio.getUserByName(name);
    }

    /**
     * Valida si un usuario existe
     * @param user_email
     * @param user_password
     * @return
     */
    public Optional<User> checkAuth(String user_email, String user_password) {
        return repositorio.checkUser(user_email, user_password);
    }
    
    /**
     * Borra todos los usuarios de la base de datos
     */
    public void deleteAll(){
        repositorio.deleteAll();;
    }
}
