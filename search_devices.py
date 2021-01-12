from miflora import miflora_scanner
from btlewrap.bluepy import BluepyBackend

print(miflora_scanner.scan(BluepyBackend))