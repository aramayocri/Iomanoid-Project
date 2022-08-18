<h1 align="center" id="title">Iomanoid, Multi-Platform NFT Directory (Multi-Marketplace)</h1>

<p align="center"><img src="https://armycrih.com/wp-content/uploads/2022/06/nft-iomanoid-genesis-collection-opensea-iomiskull-iomimon-1024x1024.png" alt="project-image"></p>

<p id="description">Iomanoid's purpose is to be the most trusted NFT directory in Latin America. We want to increase the visibility of Cryptoart or Digital Art, helping emerging and established artists with tools that allow them, from becoming visible to being able to create their own Web3 community. On the other hand, we want to help collectors to, for example, discover new talents and connect directly with them. But that's not all, we are also going to implement functionalities to Iomanoid that allow its users to learn about the technology behind NFTs and the Crypto ecosystem, Blockchain.</p>

## Features

Here're some of the project's best features:

* Post your NFT Project
* Publish your Giveaway, Whitelist or Waiting list events
* Get your "Link in Bio".
* And, if you are a collector or investor
Don't miss out on any potential projects!

## The process 
### Built with

Technologies used in the project:

*   Python
*   FastAPI
*   MySQL

### Iomanoid structure

``` Swift
// User struct
class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(45), nullable=False, unique=True)
    email = Column(String(45), nullable=False, unique=True)
    password = Column(String(25))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime)

    projects = relationship("Project", back_populates="owner")
    
    __table_args__= {
        'mysql_engine':'InnoDB'
    }
```

``` Swift
// Project struct
class Project(Base):
    __tablename__ = "projects"
    
    project_id = Column(Integer(), primary_key=True, autoincrement=True)
    project_name = Column(String(45), nullable=False, unique=True)
    description = Column(String(450), nullable=False)
    owner_id = Column(Integer(), ForeignKey("users.user_id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)
    
    owner = relationship("User", back_populates="projects")

    __table_args__= {
        'mysql_engine':'InnoDB'
    }
```

## License:

> This project is licensed under the MIT License

## Author

Made with 💚 by [armycrih](https://twitter.com/armycrih)
