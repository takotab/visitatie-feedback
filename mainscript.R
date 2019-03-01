
getinfoofparktijk <- function(code){
  stop = TRUE;i = 1;
  while(stop){
    if(table$praktijknr[i] == code){
      stop = FALSE
      infoofparktijk <- data.frame("Naam" = table$organisatienaam[i],
                                      "Telefoon" = table$telefoon[i],
                                      "Email-adres" = table$e..mail.organisatie[i],
                                      "Adres" = paste(table$adres[i],table$huisnummer[i]),
                                      "Plaats" = paste(table$postcode[i],table$plaats[i]), row.names ="Info")
      return(infoofparktijk)
    }
    i = i+1;
  }
   
}


setwd("C:/Users/Tako/Google Drive/Rugnetwerk/Visitatie")
table <- read.csv2('inschrijvingen met code en indeling voor visitatie 2016.csv',header = T)
table$achternaam <- as.character(table$achternaam)
table$organisatienaam <- as.character(table$organisatienaam)
cpraktijk = 1;
namesoftherapueten = NULL;

for(ipraktijk in 1:171){
  namesoftherapueten = NULL;
  if(is.na(table$bezoekt..praktijk[ipraktijk]) == FALSE){
    
    numoftherapeuten = 1;
    namesoftherapueten$naam[numoftherapeuten] <- paste0(table$aanhef[ipraktijk]," ",table$achternaam[ipraktijk]);
    namesoftherapueten$"Therapeut code"[numoftherapeuten]<- table$X.3[ipraktijk]
    stop <- FALSE;
    while(stop == F ){
      
      if(is.na(table$bezoekt..praktijk[ipraktijk+numoftherapeuten] )){
        
        namesoftherapueten$naam[numoftherapeuten+1] <- paste0(table$aanhef[ipraktijk+numoftherapeuten]," ",table$achternaam[ipraktijk+numoftherapeuten]);
        namesoftherapueten$"Therapeut code"[numoftherapeuten+1] <- table$X.3[ipraktijk+numoftherapeuten];
        numoftherapeuten = numoftherapeuten+1;
      }
      else{
        stop = TRUE
        
        }
    }
    namesoftherapueten <- data.frame(Naam = namesoftherapueten$naam,
                                     "Therapeut code" = namesoftherapueten$"Therapeut code")
    
    tebezoekpraktijk <- getinfoofparktijk(table$bezoekt..praktijk.met.code[ipraktijk])
    
    done[cpraktijk] = table$praktijknr[ipraktijk];
    donenaam[cpraktijk] = (table$organisatienaam[ipraktijk]);
    
    emailadressen[cpraktijk] = (table$e..mail.organisatie[ipraktijk]);
    #rmarkdown::render('Rmarkdowninvite.Rmd',  
                   #   output_file =  paste("invite_", table$praktijknr[ipraktijk], '_', Sys.Date(), ".html", sep=''), 
                  #    output_dir = "C:/Users/Tako/Google Drive/Rugnetwerk/Visitatie/invites")
    cpraktijk = cpraktijk +1;
    
  }
  
}