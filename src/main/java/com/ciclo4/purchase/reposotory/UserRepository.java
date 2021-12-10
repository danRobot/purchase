package com.ciclo4.purchase.reposotory;

import java.util.Optional;

import com.ciclo4.purchase.model.User;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface UserRepository extends MongoRepository<User,Integer>{
    @Query("{id:?0}")
    Optional<User> getUserById(Integer id);
}
