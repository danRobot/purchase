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

    public List<User> getAll(){
        return repositorio.findAll();
    }

    public Optional<User> getUser(Integer id){
        return repositorio.getUserById(id);
    }

    public void saveUser(User user){
        repositorio.save(user);
    }
}
