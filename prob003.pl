#! /usr/bin/perl -w

# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

use strict;

sub isprime {
  my $num = shift;
  my $iscomposite = 0;
  for (my $i=2; $i<=sqrt($num); $i++) {
    unless ($num % $i) {
      $iscomposite=1;
    }
  }
  return !$iscomposite;
}

#my $candidate = 13195;
my $candidate = 600851475143;
my @factors;
my $largest = 1;

for (my $i = 2; $i<=sqrt($candidate); $i++) {
  unless ($candidate % $i) {
    push(@factors, $i);
  }
}

foreach my $f (@factors) {
  $largest = $f if (isprime($f) and $f > $largest);
}

print "The largest prime factor of $candidate is $largest.\n";
