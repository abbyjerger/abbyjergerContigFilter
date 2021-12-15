/*
A KBase module: abbyjergerContigFilter
This sample module contains one small method that filters contigs.
*/

module abbyjergerContigFilter {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport for a minimum contig length
    */
    funcdef run_abbyjergerContigFilter(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

    /*
        New app using maximum contig length
    */
    funcdef run_abbyjergerContigFilter_max(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
};
