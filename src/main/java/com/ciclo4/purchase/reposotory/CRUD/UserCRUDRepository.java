package com.ciclo4.purchase.reposotory.CRUD;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.User;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface UserCRUDRepository extends MongoRepository<User,Integer>{

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
    List<User> getUserByName(String name);
    @Query("{identification:?0}")
    Optional<User> getUserByidentification(String idf);
    @Query("{monthBirthtDay:?0}")
    List<User> getUserByMonthBirthDay(String month);
}
