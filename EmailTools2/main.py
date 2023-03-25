from EmailConstructor import ConstructCopies
from EmailAnalyser import Analyse
from DomaineConstructor import ConstructCopies as _DConstructor
from DomaineAnalyser import Analyse as _DAnalyse
from GetBestEmail import Filter

origin = "TestUser" 

emails  = ConstructCopies(250, origin)

Analyse(emails)

best_email = Filter("logs/highest_logger.txt")

domaines = _DConstructor(60, best_email)

_DAnalyse(domaines)