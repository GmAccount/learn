


class Pays:
  def __init__(self,pays,population,surface):
      self.nom_du_pays=pays
      self.surface = surface
      self.population = population

  def densite(self):
      try:
        return int(self.population)/int(self.surface)
      except:
        return False

      
  def __repr__(self):
    		return "la densite de pays {} est : {:.2f}".format(self.nom_du_pays,self.densite())

