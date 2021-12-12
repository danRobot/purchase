package com.ciclo4.purchase.reposotory.CRUD;

import com.ciclo4.purchase.model.Orders;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface OrdersCRUDRepository extends MongoRepository<Orders,Integer>{
    
}
