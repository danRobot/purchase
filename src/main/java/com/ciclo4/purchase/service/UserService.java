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
    public List<User> listAllUsers(){
        return repositorio.listAll();
    }
    
    /**
     * Añade un Usuario a la base de Datos
     * @param user
     * @return
     */
    public Optional<User> insertUser(User user){
        return repositorio.postUser(user);
    }

    public Optional<User> getUserById(Integer id){
        return repositorio.getUserbyId(id);
    }

    /**
     * Busca un usuario por el Correo
     * @param email
     * @return
     */
    public Optional<User> getUserByEmail(String email){
        return repositorio.getUser(email);
    }
    public List<User> getUserByMonth(String month) {
        return repositorio.getUserByMonth(month);
    }
    /**
     * Busca un usuario por el Nombre
     * @param name
     * @return
     
    public Optional<User> getUserByName(String name){
        return repositorio.ge(name);
    }*/

    /**
     * Valida si un usuario existe
     * @param user_email
     * @param user_password
     * @return
     */
    public User checkAuth(String email, String password) {
        return repositorio.checkUser(email, password);
    }
    /**
     * Actualiza Usuario
     * @param user
     * @return
     */
    public User updateUser(User user){
        return repositorio.putUser(user);
    }
    public void deleteUser(Integer id) {
        repositorio.deleteUser(id);
    }
    public void deleteUsers(List<Integer> id) {
        repositorio.deleteUsers(id);
    }
    /**
     * Borra todos los usuarios de la base de datos
     */
    public void deleteAll(){
        repositorio.deleteAll();;
    }
}
