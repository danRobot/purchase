package com.ciclo4.purchase.model;

import java.io.Serializable;

import org.bson.types.ObjectId;
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

    @Id
    private ObjectId _id;

    //private Integer id;// (PK)AUTO_INCREMENTint(11) Not null.

    private String email;// (Unique Index)varchar(50) Not null.

    private String password;//varchar(50) Not null.
    
    private String name;//varchar(80) Not null.

    /**
     * @return the id
     *
    public Integer getId() {
        return id;
    }*/

    /**
     * @param id the id to set
     *
    public void setId(Integer id) {
        this.id = id;
    }*/

    /**
     * @return the email
     */
    public String getEmail() {
        return email;
    }

    /**
     * @param email the email to set
     */
    public void setEmail(String email) {
        this.email = email;
    }

    /**
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return the password
     */
    public String getPassword() {
        return password;
    }

    /**
     * @param password the password to set
     */
    public void setPassword(String password) {
        this.password = password;
    }

}