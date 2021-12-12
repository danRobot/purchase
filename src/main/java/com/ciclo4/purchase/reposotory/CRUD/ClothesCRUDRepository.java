package com.ciclo4.purchase.reposotory.CRUD;

import java.util.List;
import java.util.Optional;

import com.ciclo4.purchase.model.Clothes;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface ClothesCRUDRepository extends MongoRepository<Clothes,Integer>{
    /**
     * Operaciones CRUD
     * @param email
     * @return
     */
    @Query("{reference:?0}")
    Optional<Clothes> getClothesByReference(String reference);
    /*
    @Query("{email:?0}")
    Optional<Clothes> getClothesByReference(String email);
    @Query("{email:?0,password:?1}")
    Optional<Clothes> checkUser(String email,String password);
    @Query("{name:?0}")
    List<Clothes> getClothesByName(String name);
    @Query("{identification:?0}")
    Optional<Clothes> getUserByidentification(String idf);*/
}
