package com.ciclo4.purchase.reposotory;

import java.util.Optional;

import com.ciclo4.purchase.model.User;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface UserRepository extends MongoRepository<User,Integer>{

    /**
     * Operaciones CRUD
     * @param email
     * @return
     */
    @Query("{email:?0}")
    Optional<User> getUserByEmail(String email);
    @Query("{email:?0,password:?1}")
    Optional<User> checkUser(String email,String password);
    @Query("{name:?0}")
    Optional<User> getUserByName(String name);
}
