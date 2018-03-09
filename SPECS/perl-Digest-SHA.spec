%{!?perl_vendorarch: %define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)}

Name:           perl-Digest-SHA
Version:        6.01
Release:        1%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-SHA/
Source0:        http://www.cpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.003
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
Digest::SHA is written in C for speed. If your platform lacks a C compiler,
you can install the functionally equivalent (but much slower)
Digest::SHA::PurePerl module.

%define _unpackaged_files_terminate_build 0
%define _missing_doc_files_terminate_build 0 

%prep
%setup -q -n Digest-SHA-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__perl} -pi -e 's/^\tLD_RUN_PATH=[^\s]+\s*/\t/' Makefile
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check || :
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README shasum
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_mandir}/man3/*

%changelog
* Wed Mar 07 2018 Your Name <wwright@nice.com> 6.01-1
- Specfile autogenerated by cpanspec 1.78.
