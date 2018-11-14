my @vsdx_file = glob "*.vsdx";
my @docx_file = glob "*.docx";

foreach my $i(0 .. $#vsdx_file){
    rename $vsdx_file[$i] chop($vsdx_file[$i])
}

foreach my $j(0 .. $#docx_file){
    rename $docx_file[$j] chop($docx_file[$j])
}