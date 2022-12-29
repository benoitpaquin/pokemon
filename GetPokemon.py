# get list of pokemon
import pokebase as pb
chesto = pb.APIResource('berry', 'chesto')
chesto.name
'chesto'
chesto.natural_gift_type.name
'water'
charmander = pb.pokemon('charmander')  # Quick lookup.
charmander.height
6
# Now with sprites! (again!)
s1 = pb.SpriteResource('pokemon', 17)
s1.url
s2 = pb.SpriteResource('pokemon', 1, other=True, official_artwork=True)
s2.path
s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
s3.img_data