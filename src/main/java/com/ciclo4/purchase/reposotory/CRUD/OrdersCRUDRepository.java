package com.ciclo4.purchase.reposotory.CRUD;

import java.util.List;

import com.ciclo4.purchase.model.Orders;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface OrdersCRUDRepository extends MongoRepository<Orders,Integer>{
    @Query("{'salesMan.zone':?0}")
    List<Orders> getOrdersByZone(String zona);
}
