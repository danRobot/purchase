package com.ciclo4.purchase.reposotory.CRUD;

import java.util.Date;
import java.util.List;

import com.ciclo4.purchase.model.Orders;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;

public interface OrdersCRUDRepository extends MongoRepository<Orders,Integer>{
    @Query("{'salesMan.zone':?0}")
    List<Orders> getOrdersByZone(String zona);
    @Query("{'salesMan._id':?0}")
    List<Orders> getOrdersBySalesman(Integer id);
    //@Query("{registerDay:?0,'salesMan._id':?0}")
    @Query("{$and:[{'registerDay':?0},{'salesMan._id':?1}]}")
    List<Orders> getOrdersByDateAndSalesman(Date date,Integer id);
    @Query("{$and:[{'status':?0},{'salesMan._id':?1}]}")
    List<Orders> getOrdersByStatus(String status,Integer id);
}
