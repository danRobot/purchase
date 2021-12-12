package com.ciclo4.purchase.model;

import java.io.Serializable;
import java.util.Date;

//import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "users")
public class User implements Serializable{

    /*@Id
    private ObjectId _id;*/
    @Id
    private Integer id;// (PK)AUTO_INCREMENTint(11) Not null.

    private String identification;

    private String name;

    private Date birthtDay;

    private String monthBirthtDay;

    private String address;

    private String cellPhone;

    private String email;

    private String password;

    private String zone;

    private String type;
}