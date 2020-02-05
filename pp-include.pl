#!/usr/bin/perl
#
# SPDX-License-Identifier: GPL-3.0-only
# SPDX-FileCopyrightText: 2020 Alberto Pianon <pianon@array.eu>
#

use strict; 
use warnings; 

use Cwd qw(cwd);
use File::Spec;
use File::Basename;

sub begins_with
{
    return substr($_[0], 0, length($_[1])) eq $_[1];
}

sub process_file {
    my $fh = $_[0];
    my $filename = $_[1];
    my $dirname;
    my $curdir = cwd;

    if ($filename eq '') {
        $dirname = $curdir;
    } else {
        my $abs_path = File::Spec->rel2abs($filename);
        $dirname = dirname($abs_path);
        chdir($dirname);
    }
    while (my $line = <$fh>) {
        if (begins_with($line, "!include ")) {
            my $included_filename = substr($line, 9, -1); 
                # -1 because last character is newline; FIXME: does it work 
                # in Windows?
            open(my $in_fh, '<', $included_filename) 
                or die "Could not open file '$included_filename' $!";
            process_file($in_fh, $included_filename);
            chdir($dirname);
        } else {
            print $line; 
            # TODO: add a random string to footnote references in order to 
            # avoid duplicate references
        }
    }

}

if ($#ARGV == -1) {
    process_file(*STDIN, '')
} else {
    foreach (@ARGV) {
        open(my $fh, '<', $_) or die "Could not open file '$_' $!";
        process_file($fh, $_)    
    } 
}


